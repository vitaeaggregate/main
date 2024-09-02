<script lang='ts'>
	import { createEventDispatcher } from "svelte";
	import InputText from "./InputText.svelte";
	import TextArea from "./TextArea.svelte";

	let resumeID: number = 0;
	let inputName: string = '';
	let inputDescription: string = '';

	$: certificate = {
		resume: resumeID,
		name: inputName,
		inputDescription,
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
