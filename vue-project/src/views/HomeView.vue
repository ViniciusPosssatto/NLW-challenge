<template>
  <!-- <v-window v-model="window" show-arrows>
    <v-window-item v-for="n in length" :key="n">
      <v-card height="200px" class="d-flex justify-center align-center">
        <span class="text-h2">{{ n.game }}</span>
        <img :src="n.url" alt="imagem do jogo" />
      </v-card>
    </v-window-item>
  </v-window> -->
  <v-carousel 
    hide-delimiters
    :continuous="false"
    height="400"
  >
    <v-carousel-item
      v-for="(item,i) in length"
      :key="i"
      :src="item.url"
    >
    <h1>
      {{ item.game }}
    </h1>
    </v-carousel-item>
  </v-carousel>
</template>
<script>
export default {
  data: () => ({
    length: [
      {
        game: "World of Warcraft",
        url: "https://static-cdn.jtvnw.net/ttv-boxart/18122-188x250.jpg",
      },
      {
        game: "League of legends",
        url: "https://static-cdn.jtvnw.net/ttv-boxart/21779-188x250.jpg",
      },
      {
        game: "Valorant",
        url: "https://static-cdn.jtvnw.net/ttv-boxart/516575-188x250.jpg",
      },
    ],
    window: 0,
  }),
};
</script>
