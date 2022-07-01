
async function handleSubmit(evt){
    evt.preventDefault()
    // const resp = await axios.get("/check-word", { params: { word: word }});


    let word = $("word").val();

    // async function get_input(){
    //     let response = await axios.get("/submit-guess");
    // }
}

let $submit_form = $("#submit-form");

$("$submit_form").on("submit", handleSubmit())

