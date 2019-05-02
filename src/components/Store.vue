<template>
  <v-layout row justify-center>
    <v-btn
      @click.stop="dialog = true"
    >
      Saved Data
    </v-btn>

    <v-dialog
      v-model="dialog"
      max-width="290"
    >
      <v-card>
        <v-card-title class="headline">Saved data</v-card-title>

        <v-card-text>
          <ul id="example-1">
            <li v-for="item in (this.$store.state.data).slice(1)" v-bind:key="item.first">
              {{item}}
            </li>
          </ul>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="green darken-1"
            flat="flat"
            @click="dialog = false"
          >
            DOWNLOAD
          </v-btn>

          <v-btn
            color="green darken-1"
            flat="flat"
            @click="dialog = false"
          >
            Quit
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<script>
  export default {
    data () {
      return {
        dialog: false
      }
    }
  }
</script>