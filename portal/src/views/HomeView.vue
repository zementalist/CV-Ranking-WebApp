<script setup>
import axios from 'axios'
import {onMounted, ref} from 'vue';

let algorithm = ref("word2vec")
let cvs_ranked = ref({})

  onMounted(()=> {
    // resultTable = document.getElementById("result");

  })

const submitForm = () => {
  axios.get("http://127.0.0.1:8000/rank/" + algorithm.value)
  .then(response => {
    console.log(response);
    cvs_ranked.value = response.data.data
    console.log(cvs_ranked.value);
  })
}




</script>

<template>
  <div class="mt-3">
    <div class="page-content page-container mt-1" id="page-content">
      <div class="text-center">
        <label for="algorithm" class="display-4 mb-3">Select Ranking Algorithm</label>

      </div>

      <!-- <span class="publisher-btn file-group">
                  <i class="fa fa-paperclip file-browser"></i>
                  <label for="cvs_path"></label>
                  <input type="file" webkitdirectory directory name="cvs_path" />
                </span> -->
      <form @submit.prevent="submitForm" >
        <select class="form-select" aria-label="Ranker Algorithm" name="algorithm" v-model="algorithm">
        <option selected value="word2vec">Word2Vec</option>
        <option value="tfidf">TF-IDF</option>
        <option value="bm25">BM25</option>
        <!-- <option value="2">Two</option>
        <option value="3">Three</option> -->
      </select>
        <div class="text-center">
    <button class="btn btn-primary btn-block mt-3" type="submit">Rank</button>

    </div>
    </form>
      <div class="table result mt-4 text-center table-hover" v-if="Object.keys(cvs_ranked).length > 0">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col" colspan="2">CV</th>
            <th scope="col">Score</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(score,cv,index) in cvs_ranked" :key="index">
            <th scope="row">{{ index+1 }}</th>
            <td colspan="2">{{ cv }}</td>
            <td>{{ score }}%</td>
          </tr>
        </tbody>
      </div>
    </div>
  </div>
</template>

<style>

.card-bordered {
  border: 1px solid #ebebeb;
}

.card {
  border: 0;
  border-radius: 0px;
  margin-bottom: 30px;
  -webkit-box-shadow: 0 2px 3px rgba(0, 0, 0, 0.03);
  box-shadow: 0 2px 3px rgba(0, 0, 0, 0.03);
  -webkit-transition: 0.5s;
  transition: 0.5s;
}

.padding {
  padding: 3rem !important;
}

body {
  background-color: #f9f9fa;
}

.card-header:first-child {
  border-radius: calc(0.25rem - 1px) calc(0.25rem - 1px) 0 0;
}

.card-header {
  display: -webkit-box;
  display: flex;
  -webkit-box-pack: justify;
  justify-content: space-between;
  -webkit-box-align: center;
  align-items: center;
  padding: 15px 20px;
  background-color: transparent;
  border-bottom: 1px solid rgba(77, 82, 89, 0.07);
}

.card-header .card-title {
  padding: 0;
  border: none;
}

h4.card-title {
  font-size: 17px;
}

.btn-we {
  background-color: #582B8C !important;
}

.card-header > *:last-child {
  margin-right: 0;
}

.card-header > * {
  margin-left: 8px;
  margin-right: 8px;
}

.btn-secondary {
  color: #4d5259 !important;
  background-color: #e4e7ea;
  border-color: #e4e7ea;
  color: #fff;
}

.btn-xs {
  font-size: 11px;
  padding: 2px 8px;
  line-height: 18px;
}
.btn-xs:hover {
  color: #fff !important;
}

.card-title {
  font-family: Roboto, sans-serif;
  font-weight: 300;
  line-height: 1.5;
  margin-bottom: 0;
  padding: 15px 20px;
  border-bottom: 1px solid rgba(77, 82, 89, 0.07);
}

.ps-container {
  position: relative;
}

.ps-container {
  -ms-touch-action: auto;
  touch-action: auto;
  overflow: hidden !important;
  -ms-overflow-style: none;
}

.media-chat {
  padding-right: 64px;
  margin-bottom: 0;
}

.media {
  padding: 16px 12px;
  -webkit-transition: background-color 0.2s linear;
  transition: background-color 0.2s linear;
}

.media .avatar {
  flex-shrink: 0;
}

.avatar {
  position: relative;
  display: inline-block;
  width: 36px;
  height: 36px;
  line-height: 36px;
  text-align: center;
  border-radius: 100%;
  background-color: #f5f6f7;
  color: #8b95a5;
  text-transform: uppercase;
}

.media-chat .media-body {
  -webkit-box-flex: initial;
  flex: initial;
  display: table;
}

.media-body {
  min-width: 0;
}

.media-chat .media-body p {
  position: relative;
  padding: 6px 8px;
  margin: 4px 0;
  background-color: #f5f6f7;
  border-radius: 3px;
  font-weight: 100;
  color: #535353;
}

.media > * {
  margin: 0 8px;
}

.media-chat .media-body p.meta {
  background-color: transparent !important;
  padding: 0;
  opacity: 0.8;
}

.media-meta-day {
  -webkit-box-pack: justify;
  justify-content: space-between;
  -webkit-box-align: center;
  align-items: center;
  margin-bottom: 0;
  color: #8b95a5;
  opacity: 0.8;
  font-weight: 400;
}

.media {
  padding: 16px 12px;
  -webkit-transition: background-color 0.2s linear;
  transition: background-color 0.2s linear;
}

.media-meta-day::before {
  margin-right: 16px;
}

.media-meta-day::before,
.media-meta-day::after {
  content: "";
  -webkit-box-flex: 1;
  flex: 1 1;
  border-top: 1px solid #ebebeb;
}

.media-meta-day::after {
  content: "";
  -webkit-box-flex: 1;
  flex: 1 1;
  border-top: 1px solid #ebebeb;
}

.media-meta-day::after {
  margin-left: 16px;
}

.media-chat.media-chat-reverse {
  padding-right: 12px;
  padding-left: 64px;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: reverse;
  flex-direction: row-reverse;
  text-align: -webkit-right;
}

.media-chat {
  padding-right: 64px;
  margin-bottom: 0;
}

.media {
  padding: 16px 12px;
  -webkit-transition: background-color 0.2s linear;
  transition: background-color 0.2s linear;
}

.media-chat.media-chat-reverse .media-body p {
  float: right;
  clear: right;
  background-color: #582B8C;
  color: #fff;
}

.media-chat .media-body p {
  position: relative;
  padding: 6px 8px;
  margin: 4px 0;
  background-color: #f5f6f7;
  border-radius: 3px;
}

.border-light {
  border-color: #f1f2f3 !important;
}

.bt-1 {
  border-top: 1px solid #ebebeb !important;
}

.publisher {
  position: relative;
  display: -webkit-box;
  display: flex;
  -webkit-box-align: center;
  align-items: center;
  padding: 12px 20px;
  background-color: #f9fafb;
}

.publisher > *:first-child {
  margin-left: 0;
}

.publisher > * {
  margin: 0 8px;
}

.publisher-input {
  -webkit-box-flex: 1;
  flex-grow: 1;
  border: none;
  outline: none !important;
  background-color: transparent;
}

button,
input,
optgroup,
select,
textarea {
  font-family: Roboto, sans-serif;
  font-weight: 300;
}

.publisher-btn {
  background-color: transparent;
  border: none;
  color: #8b95a5;
  font-size: 16px;
  cursor: pointer;
  overflow: -moz-hidden-unscrollable;
  -webkit-transition: 0.2s linear;
  transition: 0.2s linear;
}

.file-group {
  position: relative;
  overflow: hidden;
}

.publisher-btn {
  background-color: transparent;
  border: none;
  color: #cac7c7;
  font-size: 16px;
  cursor: pointer;
  overflow: -moz-hidden-unscrollable;
  -webkit-transition: 0.2s linear;
  transition: 0.2s linear;
}


.text-info {
  color: #582B8C !important;
}
</style>