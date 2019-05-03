<template>
  <div id="team">
    <div class="Team__inner">
      <v-container >
        <v-layout>
          
            <!-- gert -->
       
              <v-card width="100%">
                <v-img
                  :src="require('../assets/gert.jpg')"
                  height="300px"
                  position="top"
                >
                </v-img>
              
              <v-card-title primary-title>
                <div>
                  <h3 class="headline mb-2">Gert Cheedz</h3>
                  <div> {{ card_gert }} </div>
                </div>
              </v-card-title>
              </v-card>
            
            <!-- isaiah -->
            <v-card width="100%">
              <v-img
                :src="require('../assets/ish.jpg')"
                height="300px"
                position="top"

              >
              </v-img>

            <v-card-title primary-title>
              <div>
                <h3 class="headline mb-2">Isaiah Evans</h3>
                <div> {{ card_ish }} </div>
              </div>
            </v-card-title>
            </v-card>

            <!-- andrew -->
            <v-card width="100%">
              <v-img
                :src="require('../assets/andrew.jpg')"
                height="300px"
                position="top"

              >
              </v-img>

            <v-card-title primary-title>
              <div>
                <h3 class="headline mb-2">Andrew Lewis</h3>
                <div> {{ card_andrew }} </div>
              </div>
            </v-card-title>
            </v-card>

            <!-- mike -->
            <v-card width="100%">
              <v-img
                :src="require('../assets/mike.jpg')"
                height="300px"
                position="top"

              >
              </v-img>

            <v-card-title primary-title>
              <div>
                <h3 class="headline mb-2">Mike Streinz</h3>
                <div> {{ card_mike }} </div>
              </div>
            </v-card-title>
            </v-card>

            <!-- lvn -->
            <v-card width="100%">
              <v-img
                :src="require('../assets/lvn.jpg')"
                height="300px"
                position="top"

              >
              </v-img>

            <v-card-title primary-title>
              <div>
                <h3 class="headline mb-2">Lavon Bergo</h3>
                <div> {{ card_lvn }} </div>
              </div>
            </v-card-title>
            </v-card>

        </v-layout>
      </v-container>
    </div>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        card_gert: 'Garrett is a Junior at HMC majoring in CS / Math',
        card_ish: 'Isaiah is a Junior at HMC majoring in CS',
        card_andrew: 'Andrew a Junior at CMC majoring in CS at HMC',
        card_mike: 'Mike a Junior at HMC majoring in CS / Math',
        card_lvn: 'Lavon a Junior at HMC majoring in CS'
      }
    }
  }
</script>

<style lang="scss">

.v-card {
  margin: 0.5rem;
}

.Team {

  &__inner {

    &__people {
      padding: 2rem;
    }
  }
}
</style>
