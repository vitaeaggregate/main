<script lang='ts'>
	import { createEventDispatcher } from "svelte";
	import InputText from "$lib/components/InputText.svelte";
	import InputDate from "$lib/components/InputDate.svelte";
	
	let headerId: number;
	let inputTitle: string;
	let inputSubTitle: string;
	let inputStartDate: string;
	let inputEndDate: string;
	let inputDescription: string;

	$: project = {
		header: headerId,
		title: inputTitle,
		sub_title: inputSubTitle,
		start_date: inputStartDate,
		end_date: inputEndDate,
		description: inputDescription,
	}

	const dispatch = createEventDispatcher();
	$: {
		dispatch("update", project)
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
