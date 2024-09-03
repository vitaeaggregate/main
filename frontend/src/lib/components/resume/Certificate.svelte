<script lang='ts'>
	import { createEventDispatcher } from "svelte";
	import InputText from "$lib/components/InputText.svelte";
	import TextArea from "$lib/components/TextArea.svelte";

	let headerId: number;
	let inputName: string;
	let inputDescription: string;

	$: certificate = {
		header: headerId,
		name: inputName,
		description: inputDescription,
	}

	const dispatch = createEventDispatcher();
	$: {
		dispatch("update", certificate)
	}
</script>

<div class="flex flex-col">
	<h2>Certificate</h2>
	<InputText label="Name" bind:value={inputName}/>
	<TextArea label="Description" bind:value={inputDescription}/>
</div>
