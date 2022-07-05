const $guesses = $(".guesses");

$("#submit-form").on("submit", async function(e) {
    e.preventDefault();
    console.log("prevent default")

    let $word = $("#ch-word").val();
    console.log($word);
    const resp = await axios.get("/check_word", { params: { word: $word }});
    console.log(resp);
    console.log("result:", resp.data.result)

    console.log("$guesses", $guesses);
    // $guesses.innerHTML = "";
    $guesses.append(`${$word}<br>`);
    $("#ch-word").val('');
})
