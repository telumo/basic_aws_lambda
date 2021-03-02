<template>
    <div>
        <h2 class="eng">{{ question }}</h2>
        <hr>
        <h3 class="ee">Sinu Vastus</h3>
        <textarea name="ans" id="ans" cols="30" rows="8" class="ee"></textarea>
    </div>
</template>

<script>
export default {
    name: "QA",
    props: {
        question: String
    }
}
</script>

<style scoped>
    @font-face {
        font-family: "AinoR";
        src: url("../assets/Aino-Regular.woff");
    }
    @font-face {
        font-family: "AinoH";
        src: url("../assets/Aino-Headline.woff");
    }
    h2, h3 {
        margin: auto;
        text-align: center;
    }
    h3 {
        margin-bottom: 10px;
    }
    textarea {
        display: block;
        margin: 0 auto;
        text-align: center;
        font-size: 20px;
        border-radius: 5px;
    }
    .eng {
        font-family: "AinoR";
        font-weight: lighter;
    }
    .ee {
        font-family: "AinoH";
    }
</style>