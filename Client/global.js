const global_NS = {}

global_NS.show = function (status, message) {
    toastr.options = {
        "closeButton": true,
        "debug": false,
        "newestOnTop": false,
        "progressBar": false,
        "positionClass": "toast-top-right",
        "preventDuplicates": true,
        "onclick": null,
        "showDuration": "300",
        "hideDuration": "100",
        "timeOut": "2500",
        "extendedTimeOut": "1000",
        "showEasing": "linear",
        "hideEasing": "linear",
        "showMethod": "slideDown",
        "hideMethod": "slideUp"
    };
    toastr[status](message);
};

global_NS.isInteger = function(str) {
    return str === parseInt(str, 10)
}



function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function demo() {
    console.log('Taking a break...');
    await sleep(2000);
    console.log('Two seconds later, showing sleep in a loop...');

    // Sleep in loop
    for (let i = 0; i < 5; i++) {
        if (i === 3)
            await sleep(2000);
        console.log(i);
    }
}
