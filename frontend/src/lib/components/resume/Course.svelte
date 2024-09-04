<script lang="ts">
	import InputText from "$lib/components/InputText.svelte";
	import InputDate from "$lib/components/InputDate.svelte";
	import TextArea from "$lib/components/TextArea.svelte";

	export let value = {};

	let inputDegree: string = "";
	let inputInstitution: string = "";
	let inputCity: string = "";
	let inputCountry: string = "";
	let inputStartDate: Date;
	let inputEndDate: Date;
	let inputDescription: string = "";

	$: value = {
		degree: inputDegree,
		institution: inputInstitution,
		city: inputCity,
		country: inputCountry,
		start_date: inputStartDate,
		end_date: inputEndDate,
		description: inputDescription
	};
</script>

<div class="flex flex-col">
	<h2>Course</h2>
	<InputText label="Degree" bind:value={inputDegree} />
	<InputText label="Institution" bind:value={inputInstitution} />
	<InputText label="City" bind:value={inputCity} />
	<InputText label="Country" bind:value={inputCountry} />
	<InputDate label="Start Date" bind:value={inputStartDate} />
	<InputDate label="End Date" bind:value={inputEndDate} />
	<TextArea label="Description" bind:value={inputDescription} />
</div>
