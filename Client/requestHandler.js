const requestHandler = {};
requestHandler.apiDomain = "http://localhost:5000";

requestHandler.send = function (data = {}, route, successFunc, errorFunc, completeFunc, method = 'POST') {
    var settings = {
        "url": requestHandler.apiDomain  + route,
        "method": method,
        "headers": {
            "Content-Type": "application/json"
        },
        "data": JSON.stringify(data),
        success: successFunc,
        error: errorFunc,
        complete: completeFunc
    };
    $.ajax(settings);
}
