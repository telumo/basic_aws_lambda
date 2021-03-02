<template>
  <div class="wrap">
    <Navbar title="Eesti Kott"/>
    <div class="image"></div>
    <div class="container">
      <Header title="Kuidas on eesti keeles?"/>
      <QA question="Hello"/>
    </div>
  </div>
</template>

<script>
import Header from "./components/Header"
import Navbar from "./components/Navbar"
import QA from "./components/QA"

export default {
  name: 'App',
  components: {
    Header,
    Navbar,
    QA
  }
}
</script>

<style>
  .wrap {
    position: relative;
    height: 100%;
  }
  .container {
    max-width: 500px;  
    margin: 0;
    overflow: auto;
    min-height: 300px;
    padding: 30px;
    border-radius: 5px;
    background-color: rgba(255, 255, 255, 0.3);
    position: absolute;
    top: 550%;
    left: 100px;
  }
  .image {
    height: 900px;
    width: 100%;
    position: absolute;
    top: 0;
    z-index: -1; 
    background-image: url("./assets/Moose_Kalle_Pihelgas_cropped.jpg");
    background-repeat: no-repeat;
    background-position: center center;
    background-attachment: fixed;
  }

</style>
