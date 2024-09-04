<script lang='ts'>
	import { createEventDispatcher } from "svelte";
	import InputText from "$lib/components/InputText.svelte";
	import InputDate from "$lib/components/InputDate.svelte";
	import TextArea from "$lib/components/TextArea.svelte";

	let headerId: number;
	let inputDegree:string;
	let inputInstitution:string;
	let inputCity:string;
	let inputCountry:string;
	let inputStartDate:string;
	let inputEndDate:string;
	let inputDescription: string

	$: education = {
		header: headerId,
		degree: inputDegree,
		institution: inputInstitution,
		city: inputCity,
		country: inputCountry,
		start_date: inputStartDate,
		end_date: inputEndDate,
		description: inputDescription,
	}

	const dispatch = createEventDispatcher();
	$: {
		dispatch("update", education);
	}
</script>

<div class="flex flex-col">
	<h2>Education</h2>
	<InputText label="Degree" bind:value={inputDegree}/>
	<InputText label="Institution" bind:value={inputInstitution}/>
	<InputText label="City" bind:value={inputCity}/>
	<InputText label="Country" bind:value={inputCountry}/>
	<InputDate label="Start Date" bind:value={inputStartDate}/>
	<InputDate label="End Date" bind:value={inputEndDate}/>
	<TextArea label="Description" bind:value={inputDescription}/>
</div>
