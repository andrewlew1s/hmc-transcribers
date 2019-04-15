<template>
	<div class="Page2">
			<div class="Page2__header">
				<h1>{{data.type}}</h1>
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
				type: this.$store.state.data.type,
				confidence: this.$store.state.confidence,
				end_pos: this.$store.state.data.end_pos,
				start_pos: this.$store.state.data.start_pos,
				text: this.$store.state.data.text
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
