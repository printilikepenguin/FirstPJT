<template>
  <div class="containerbody">
    <div class="titlepart">
      <h1 class="title">환율 계산기</h1>
    </div>
    <!-- <div class="calculatortitle">환율 계산기</div> -->
    <Currency />
  </div>
</template>

<script setup>
import Currency from "@/components/ExchangeViewComponents/Currency.vue";
</script>

<style scoped>
.containerbody {
  width: 100%;
  height: 91vh;
  background-color: whitesmoke;
  /* background-image: linear-gradient(
      rgba(255, 255, 255, 0.4),
      rgba(255, 255, 255, 0.4)
    ),
    url("@/assets/backgroundimg.png"); */

  background-size: cover;
  background-repeat: no-repeat;
  display: flex;
  flex-direction: column;
  /* justify-content: center; */
  align-items: center;
}

/* .calculatortitle {
  width: 100%;
  text-align: center;
  margin: 30px 0px;
  font-size: 3rem;
  font-weight: 400;
  font-family: "Noto Sans KR", sans-serif;
  color: rgb(0, 53, 133);
  border-bottom: 1px solid grey;
  padding-bottom: 30px;
} */

.titlepart {
  width: 100%;
  height: 200px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 30px;
  border-bottom: 2px solid lightgray;
}

.title {
  margin-top: 40px;
  font-size: 3rem;
  font-weight: 500;
  font-family: 'Noto Sans KR', sans-serif;
  color: rgb(0, 53, 133);
}
</style>
