<template>
	<div class="Page2">
		<div class="Page2__results">
			<v-data-table
				:headers="headers"
				:items="fields"
				class="elevation-1"
				hide-actions>
				<template v-slot:items="props">
					<td>{{ props.item.first }}</td>
					<td>{{ props.item.last }}</td>
					<td>{{ props.item.email }}</td>
					<td>{{ props.item.address }}</td>
					<td>{{ props.item.address2 }}</td>
					<td>{{ props.item.phone }}</td>
					<td>{{ props.item.fax }}</td>
					<td>{{ props.item.city }}</td>
					<td>{{ props.item.state }}</td>
					<td>{{ props.item.zip }}</td>
					<td>{{ props.item.country }}</td>
					<td>{{ props.item.title }}</td>
					<td>{{ props.item.company }}</td>
				</template>
			</v-data-table>
		</div>
		<div class="Page2__header">
			<h2>Try again, save or view your data</h2>
		</div>
		<div class="Page2__buttons">
			<v-btn @click="exportData">Save</v-btn>
			<v-btn to="/">Try again</v-btn>
			<Store />	
		</div>		
	</div>
</template>

<script>
import Store from '../../components/Store.vue'
import { mapState } from 'vuex'

export default {
	data () {
      return {
        headers: [
			{ text: 'First Name', value: 'first' },
			{ text: 'Last Name', value: 'last' },
			{ text: 'Email', value: 'email' },     
			{ text: 'Address', value: 'address' },
			{ text: 'Address2', value: 'address2' },
			{ text: 'Phone', value: 'phone' },
			{ text: 'Fax', value: 'fax' },
			{ text: 'City', value: 'city' },
			{ text: 'State', value: 'state' },
			{ text: 'Zip', value: 'zip' },
			{ text: 'Country', value: 'country' },
			{ text: 'Title', value: 'title' },
			{ text: 'Company', value: 'company' }
        ],
        fields: [
			{
				first: this.$store.state.data.first,
				last: this.$store.state.data.last,
				email: this.$store.state.data.email,
				address: this.$store.state.data.address,
				address2: this.$store.state.data.address2,
				phone: this.$store.state.data.phone,
				fax: this.$store.state.data.fax,
				city: this.$store.state.data.city,
				state: this.$store.state.data.state,
				zip: this.$store.state.data.zip,
				country: this.$store.state.data.country,
				title: this.$store.state.data.title,
				company: this.$store.state.data.company
			}
		]
      }
		},
	components: {
		Store
	},
	methods: {
		exportData(){
			this.$store.commit('addData', this.fields)
		}
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

	&__results {
		padding: 1rem;
	}

	&__card {
		padding: 1rem;
	}
	
	&__header {
		padding: 2rem;
	}

	&__buttons {
		padding: 1rem;
	}
}
</style>
