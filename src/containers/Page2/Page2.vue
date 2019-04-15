<template>
	<div class="Page2">
		<div class="Page2__card">
				<v-layout>
					<v-flex xs12 sm6 offset-sm3>
						<v-card>
							<v-img
								height="200px"
								src="https://images.pexels.com/photos/326569/pexels-photo-326569.jpeg?cs=srgb&dl=adult-blank-business-326569.jpg&fm=jpg">
								<v-container fill-height fluid>
								</v-container>
							</v-img>
							<v-card-actions>
								<v-btn flat color="black">Share</v-btn>
								<v-btn @click="updateData" flat color="black">Explore</v-btn>
							</v-card-actions>
						</v-card>
					</v-flex>
				</v-layout>
			</div>
			<div class="Page2__header">
				<h1>{{data}}</h1>
			</div>
			<v-data-table
				:headers="headers"
				:items="fields"
				class="elevation-1">
				<template v-slot:items="props">
					<!-- <td>{{ props.item.name }}</td> -->
					<td>{{ props.item.type }}</td>
					<td>{{ props.item.confidence }}</td>
					<td>{{ props.item.end_pos }}</td>
					<td>{{ props.item.start_pos }}</td>
					<td>{{ props.item.text }}</td>
				</template>
			</v-data-table>
			<div class="Page2__header">
				<h2>Or try again with another card:</h2>
			</div>
			<Browse />
	</div>
</template>

<script>
import axios from 'axios'
import Browse from '../../components/Browse.vue'
import { mapState } from 'vuex'

export default {
	data () {
      return {
        headers: [
			{
			text: 'Type',
			align: 'left',
			// sortable: false,
			value: 'type'
			},
			{ text: 'Confidence', value: 'confidence' },
			{ text: 'Start Position', value: 'start_pos' },
			{ text: 'End Position', value: 'end_pos' },     
			{ text: 'Text', value: 'text' }
        //   { text: 'Type', value: 'type' }
        ],
        fields: [
			{
				type: 'he',
				confidence: this.$store.state.data,
				end_pos: 'hi',
				start_pos: 'hi',
				text: 'hi',
			}
		]
      }
		},
	components: {
		Browse
	},

	computed: {
		...mapState([
			'data'
		])
	},

	methods: {		
		updateData() {
			axios.get('http://127.0.0.1:5000/first')
			.then(res => {
				console.log(res.data)
				var resString = JSON.stringify(res.data)
				this.$store.commit('updateData',resString)
			})
		}
	}
}
</script>

<style lang="scss">
@import '../../settings';

.Page2 {

	&__card {
		padding: 1rem;
	}
	
	&__header{
		padding: 2rem;
	}
}
</style>
