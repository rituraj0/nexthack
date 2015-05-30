$(document).ready(function(){
	
	//initializing preference values in care they are not set.
	if(!localStorage.HACKEREARTHhiring)localStorage.HACKEREARTHhiring = "true";
	if(!localStorage.HACKEREARTHcontest)localStorage.HACKEREARTHcontest = "true";
	if(!localStorage.HACKERRANK)localStorage.HACKERRANK = "true";
	if(!localStorage.CODECHEF)localStorage.CODECHEF = 'true';
	if(!localStorage.CODEFORCES)localStorage.CODEFORCES = 'true';
	if(!localStorage.TOPCODER)localStorage.TOPCODER = 'true';
	if(!localStorage.GOOGLE)localStorage.GOOGLE = 'true';
	if(!localStorage.OTHER)localStorage.OTHER = 'true';

	if(!localStorage.CHECKINTERVAL)localStorage.CHECKINTERVAL = 5;

	$('#Hackerearthhiring')[0].checked 	= ( localStorage.HACKEREARTHhiring=="true" );
	$('#Hackerearthcontest')[0].checked = ( localStorage.HACKEREARTHcontest=="true" );
	$('#Hackerrank')[0].checked 		= ( localStorage.HACKERRANK=="true" );
	$('#Codechef')[0].checked 			= ( localStorage.CODECHEF=="true" );
	$('#Codeforces')[0].checked 		= ( localStorage.CODEFORCES=="true" );
	$('#Topcoder')[0].checked 			= ( localStorage.TOPCODER=="true" );
	$('#Google')[0].checked 			= ( localStorage.GOOGLE=="true" );
	$('#Other')[0].checked 				= ( localStorage.OTHER=="true" );

	$('#checkInterval')[0].value = localStorage.CHECKINTERVAL;

	$(':checkbox').change( function(){
		localStorage.HACKEREARTHhiring  = $('#Hackerearthhiring')[0].checked;
		localStorage.HACKEREARTHcontest = $('#Hackerearthcontest')[0].checked;
		localStorage.HACKERRANK 		= $('#Hackerrank')[0].checked;
		localStorage.CODECHEF 			= $('#Codechef')[0].checked;
		localStorage.CODEFORCES 		= $('#Codeforces')[0].checked;
		localStorage.TOPCODER 			= $('#Topcoder')[0].checked;
		localStorage.GOOGLE 			= $('#Google')[0].checked;
		localStorage.OTHER	 			= $('#Other')[0].checked;
	});
	
	$('#checkInterval').change(function(){
		localStorage.CHECKINTERVAL = $('#checkInterval')[0].value;
	});
});