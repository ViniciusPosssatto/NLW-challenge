<!-- eslint-disable prettier/prettier -->
<template>
    <v-container
      class="mx-auto"
    >
    <v-form
    ref="form"
    v-model="form"
    class="pa-12 pt-6"
    >
    <v-row>
        <v-col
            cols="5"
        >
        <v-text-field
          v-model="name"
          filled
          color="deep-purple"
          label="Name"
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
        <v-text-field
          v-model="discord"
          filled
          color="deep-purple"
          label="Discord user"
          type="text"
        ></v-text-field>        
        <v-checkbox
          v-model="agreement"
          :rules="[rules.required]"
          color="deep-purple"
          style="margin-top: 62px;"
        >
          <template v-slot:label>
            I agree to the&nbsp;
            <a
              href="#"
              @click.stop.prevent="dialog = true"
            >Terms of Service</a>
            &nbsp;and&nbsp;
            <a
              href="#"
              @click.stop.prevent="dialog = true"
            >Privacy Policy</a>*
          </template>
        </v-checkbox>
        </v-col>
        <v-col
            cols="5"
        >
        <v-select
          v-model="game"
          filled
          color="deep-purple"
          label="Game"
          type="text"
        ></v-select>
        <v-text-field
          v-model="hoursPlaying"
          filled
          color="deep-purple"
          label="Hours playing"
          type="number"
        ></v-text-field>
        <v-select
          v-model="days"
          filled
          color="deep-purple"
          label="Week days"
          type="text"
        ></v-select>
        <v-text-field
          v-model="hoursStart"
          filled
          color="deep-purple"
          label="Hours start"
          type="number"
        ></v-text-field>
        <v-text-field
          v-model="hoursEnd"
          filled
          color="deep-purple"
          label="Hours end"
          type="number"
        ></v-text-field>
        </v-col>
    </v-row>
      </v-form>
      <v-divider></v-divider>
      <v-card-actions>
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
      <v-dialog
        v-model="dialog"
        absolute
        max-width="400"
        persistent
      >
      </v-dialog>
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