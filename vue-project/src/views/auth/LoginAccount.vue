<!-- eslint-disable prettier/prettier -->
<template>
    <v-container
      class="mx-auto"
    >
    <v-row>
      <v-col
        cols="6"
      >

      <v-form
        ref="form"
        v-model="form"
        class="pa-12 pt-6"
        style="max-width: 600px;"
      >
        <v-text-field
          v-model="discord"
          filled
          color="deep-purple"
          label="Discord user"
          type="text"
        ></v-text-field>
        <v-text-field
          v-model="password"
          :rules="[rules.password, rules.length(6)]"
          filled
          color="deep-purple"
          counter="6"
          label="Password"
          style="min-height: 96px"
          type="password"
        ></v-text-field>
      </v-form>
      <v-divider
        style="max-width: 600px;"
      ></v-divider>
      <v-card-actions
      style="max-width: 600px;"
      >
        <v-btn
          text
          @click="$refs.form.reset()"
        >
          Clear
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn
          :disabled="!form"
          :loading="isLoading"
          class="white--text"
          color="deep-purple accent-4"
          depressed
        >
          Submit
        </v-btn>
      </v-card-actions>
      </v-col>
      <v-col
        cols="6"
      >
      <img src="../../assets/images/Wallpaper - 1920x1080.png" alt="" style="max-width: 600px; border-style: groove; border-radius: 20px;">
      </v-col> 
      </v-row>
    </v-container>
</template>
<script>
/* eslint-disable prettier/prettier */
    export default {
      data: () => ({
        agreement: false,
        bio: 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts',
        dialog: false,
        email: undefined,
        form: false,
        isLoading: false,
        password: undefined,
        phone: undefined,
        rules: {
          email: v => !!(v || '').match(/@/) || 'Please enter a valid email',
          length: len => v => (v || '').length >= len || `Invalid character length, required ${len}`,
          password: v => !!(v || '').match(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*(_|[^\w])).+$/) ||
            'Password must contain an upper case letter, a numeric character, and a special character',
          required: v => !!v || 'This field is required',
        },
      }),
    }
  </script>