/*
 ** Setting default
 ** parameter for datatable
 */
var oDefaultDTConfig;
//var fnDelete = null;

//DataTable.push("fnDelete");
(function($) {

	oDefaultDTConfig = {
		"searching" : false,
		"bProcessing" : true,
		"serverSide" : true,
		"order" : [ 1, 'asc' ],
		"sDom" : 'T<"clear">lfrtip',
		"oTableTools" : {
			"sRowSelect" : "multi",
			"sRowSelector" : 'td:first-child',
			"aButtons" : [ "select_all", "select_none" ],
			"sSwfPath" : "{{url_for('static', filename='vendors/datatables-1.10.1/exts/TableTools/swf/copy_csv_xls_pdf.swf')}}"
		}
	};

}(jQuery));