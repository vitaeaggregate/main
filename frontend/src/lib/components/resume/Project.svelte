<script lang='ts'>
	import InputText from "$lib/components/InputText.svelte";
	import InputDate from "$lib/components/InputDate.svelte";
	
	export let value = {}

	let inputTitle: string = "";
	let inputSubTitle: string = "";
	let inputStartDate: Date;
	let inputEndDate: Date;
	let inputDescription: string = "";

	$: value = {
		title: inputTitle,
		sub_title: inputSubTitle,
		start_date: inputStartDate,
		end_date: inputEndDate,
		description: inputDescription,
	}
</script>

<div class="flex flex-col">
	<h2>Projects</h2>
	<InputText label="Title" bind:value={inputTitle}/>
	<InputText label="Subtitle" bind:value={inputSubTitle}/>
	<InputDate label="Start Date" bind:value={inputStartDate}/>
	<InputDate label="End Date" bind:value={inputEndDate}/>
	<InputText label="Description" bind:value={inputDescription}/>
</div>
