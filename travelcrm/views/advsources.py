# -*-coding: utf-8-*-

import logging
import colander

from pyramid.view import view_config

from ..models import DBSession
from ..models.advsource import Advsource
from ..lib.qb.advsources import AdvsourcesQueryBuilder

from ..forms.advsources import AdvsourceSchema


log = logging.getLogger(__name__)


class Advsources(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @view_config(
        context='..resources.advsources.Advsources',
        request_method='GET',
        renderer='travelcrm:templates/advsources/index.mak',
        permission='view'
    )
    def index(self):
        return {}

    @view_config(
        name='list',
        context='..resources.advsources.Advsources',
        xhr='True',
        request_method='POST',
        renderer='json',
        permission='view'
    )
    def list(self):
        qb = AdvsourcesQueryBuilder(self.context)
        qb.search_simple(
            self.request.params.get('search'),
        )
        qb.sort_query(
            self.request.params.get('sort'),
            self.request.params.get('order', 'asc')
        )
        qb.page_query(
            int(self.request.params.get('rows')),
            int(self.request.params.get('page'))
        )
        return {
            'total': qb.get_count(),
            'rows': qb.get_serialized()
        }

    @view_config(
        name='add',
        context='..resources.advsources.Advsources',
        request_method='GET',
        renderer='travelcrm:templates/advsources/form.mak',
        permission='add'
    )
    def add(self):
        _ = self.request.translate
        return {'title': _(u'Add Advertising Source')}

    @view_config(
        name='add',
        context='..resources.advsources.Advsources',
        request_method='POST',
        renderer='json',
        permission='add'
    )
    def _add(self):
        _ = self.request.translate
        schema = AdvsourceSchema().bind(request=self.request)

        try:
            controls = schema.deserialize(self.request.params)
            advsource = Advsource(
                name=controls.get('name'),
                resource=self.context.create_resource(controls.get('status'))
            )
            DBSession.add(advsource)
            return {'success_message': _(u'Saved')}
        except colander.Invalid, e:
            return {
                'error_message': _(u'Please, check errors'),
                'errors': e.asdict()
            }

    @view_config(
        name='edit',
        context='..resources.advsources.Advsources',
        request_method='GET',
        renderer='travelcrm:templates/advsources/form.mak',
        permission='edit'
    )
    def edit(self):
        _ = self.request.translate
        advsource = Advsource.get(self.request.params.get('id'))
        return {'item': advsource, 'title': _(u'Edit Advertising Source')}

    @view_config(
        name='edit',
        context='..resources.advsources.Advsources',
        request_method='POST',
        renderer='json',
        permission='edit'
    )
    def _edit(self):
        _ = self.request.translate
        schema = AdvsourceSchema().bind(request=self.request)
        advsource = Advsource.get(self.request.params.get('id'))
        try:
            controls = schema.deserialize(self.request.params)
            advsource.name = controls.get('name')
            advsource.resource.status = controls.get('status')
            return {'success_message': _(u'Saved')}
        except colander.Invalid, e:
            return {
                'error_message': _(u'Please, check errors'),
                'errors': e.asdict()
            }

    @view_config(
        name='delete',
        context='..resources.advsources.Advsources',
        request_method='GET',
        renderer='travelcrm:templates/advsources/delete.mak',
        permission='delete'
    )
    def delete(self):
        return {
            'rid': self.request.params.get('rid')
        }

    @view_config(
        name='delete',
        context='..resources.advsources.Advsources',
        request_method='POST',
        renderer='json',
        permission='delete'
    )
    def _delete(self):
        _ = self.request.translate
        for id in self.request.params.getall('id'):
            advsource = Advsource.get(id)
            if advsource:
                DBSession.delete(advsource)
        return {'success_message': _(u'Deleted')}