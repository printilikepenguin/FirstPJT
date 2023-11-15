<template>
    <table class="table">
      <thead>
        <th>번호</th>
        <th>분류</th>
        <th>제목</th>
        <th>작성자</th>
        <th>작성일</th>
      </thead>
      <tbody>
      <tr v-for="article in store.articles" :key="article.id">
        <td>{{ article.id}}</td>
        <td>{{ article.category }}</td>
        <td>
          <RouterLink :to="{ name: 'ArticleDetailView', params: { id: article.id }}">
            <p>{{ article.title }}</p>
          </RouterLink>
        </td>
        <td><!-- <p>{{ article.users }}</p> --></td>
        <td>{{ article.created_at }}</td>
      </tr>
    </tbody>
    </table>
  </template>
  
  <script setup>
  import { useCounterStore } from '@/stores/counter';
  import { RouterLink } from 'vue-router'
  
  const store = useCounterStore()
  defineProps({
    article: Object
  })
  
  </script>
  
  <style>
  .table {   
    text-align: center;
  }
  </style>