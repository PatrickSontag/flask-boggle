const $guesses = $(".guesses");
const $score = $(".score");
let score = 0;

$("#submit-form").on("submit", async function(e) {
    e.preventDefault();
    console.log("prevent default")

    let $word = $("#ch-word").val();
    console.log($word);
    const resp = await axios.get("/check_word", { params: { word: $word }});
    const result = resp.data.result;
    console.log(resp);
    console.log("result:", resp.data.result)

    console.log("$guesses", $guesses);
    // $guesses.innerHTML = "";
    $guesses.append(`<b>${$word}</b> - ${result}<br>`);
    $("#ch-word").val('');

    if (result === "ok") {
        console.log("score points:", $word.length);
        score += $word.length;
        $score.html(`<h3>Score: ${score}</h3>`)
    }
})
