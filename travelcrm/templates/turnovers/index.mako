<%namespace file="../common/search.mako" import="searchbar"/>
<%namespace file="../common/context_info.mako" import="context_info"/>
<%
    _id = h.common.gen_id()
    _t_id = "t-%s" % _id
    _tb_id = "tb-%s" % _id
    _s_id = "s-%s" % _id    
%>
<div class="easyui-panel unselectable"
    data-options="
        fit:true,
        border:false,
        iconCls:'fa fa-pie-chart',
        tools:'#${_t_id}'
    "
    title="${_(u'Turnovers')}">
    ${context_info(_t_id, request)}
    <table class="easyui-datagrid"
        id="${_id}"
        data-options="
            url:'${request.resource_url(_context, 'list')}',border:false,
            pagination:true,fit:true,pageSize:50,singleSelect:true,
            rownumbers:true,sortName:'id',sortOrder:'desc',
            pageList:[50,100,500],idField:'_id',checkOnSelect:false,
            selectOnCheck:false,toolbar:'#${_tb_id}',
            onBeforeLoad: function(param){
                var dg = $(this);
                $.each($('#${_s_id}, #${_tb_id} .searchbar').find('input'), function(i, el){
                    param[$(el).attr('name')] = $(el).val();
                });
            }
        " width="100%">
        <thead>
            <th data-options="field:'id',sortable:true,width:50">${_(u"id")}</th>
            <th data-options="field:'name',sortable:true,width:200">${_(u"name")}</th>
            <th data-options="field:'sum_to',sortable:true,width:100">${_(u"sum to")}</th>
            <th data-options="field:'sum_from',sortable:true,width:100">${_(u"sum from")}</th>
			<th data-options="field:'balance',sortable:true,width:100">${_(u"balance")}</th>
            <th data-options="field:'currency',sortable:true,width:80">${_(u"currency")}</th>
        </thead>
    </table>

    <div class="datagrid-toolbar" id="${_tb_id}">
        <div class="actions button-container dl45">
            <script type="text/javascript">
            	function get_params_${_id}(use_sort_options){
            		var obj = $('#${_tb_id}');
            		var params = new Object();
            		$.each($('#${_s_id}, #${_tb_id} .searchbar').find('input'), function(i, el){
                        params[$(el).attr('name')] = $(el).val();
                    });
            		if(use_sort_options){
            			var dg_options = $('#${_id}').datagrid('options');
            			params['sort'] = dg_options.sortName;
            			params['order'] = dg_options.sortOrder;
            		}
            		return $.param(params, true);
            	}
            </script>
            <div class="button-group">
	            % if _context.has_permision('view'):
	            <a href="#" class="button _action" 
	                data-options="container:'#${_id}',action:'dialog_open',property:'with_row',url:'${request.resource_url(_context, 'cashflows')}',params_str:get_params_${_id}(false)">
	                <span class="fa fa-lightbulb-o"></span>${_(u'Cashflows')}
	            </a>
	            <a href="#" class="button _action" 
	                data-options="container:'#${_id}',action:'blank_open',url:'${request.resource_url(_context, 'export', query={'export': True})}',params_str:get_params_${_id}(true)">
	                <span class="fa fa-file-pdf-o"></span>${_(u'Export To PDF')}
	            </a>
                % endif
            </div>
        </div>
        <div class="ml45 tr">
            <div class="search">
                ${searchbar(_id, _s_id, prompt=_(u'Enter name of account or subaccount or account item'))}
                <div class="advanced-search tl hidden" id = "${_s_id}">
                    <div>
                        ${h.tags.title(_(u"report by"))}
                    </div>
                    <div>
                        ${h.tags.select(
                        	'report_by',
                        	'account',
                        	[('account', _(u'Account')), ('subaccount', _(u'Subaccount'))],
                        	class_='easyui-combobox w20',
                        	data_options="panelHeight:'auto'"
                        )}
                    </div>
                    <div class="mt05">
                        ${h.tags.title(_(u"currency"))}
                    </div>
                    <div>
                        ${h.fields.currencies_combogrid_field(
                            request, 'currency_id', show_toolbar=False
                        )}
                    </div>
                    <div class="mt05">
                        ${h.tags.title(_(u"dates"))}
                    </div>
                    <div>
                        ${h.fields.date_field('date_from')}
                        <span class="p1">-</span>
                        ${h.fields.date_field('date_to')}
                    </div>
                    <div class="mt1">
                        <div class="button-group minor-group">
                            <a href="#" class="button _advanced_search_submit">${_(u"Find")}</a>
                            <a href="#" class="button" onclick="$(this).closest('.advanced-search').hide();">${_(u"Close")}</a>
                            <a href="#" class="button danger _advanced_search_clear">${_(u"Clear")}</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>