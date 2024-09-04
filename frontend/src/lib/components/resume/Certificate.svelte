<script lang='ts'>
	import InputText from "$lib/components/InputText.svelte";
	import TextArea from "$lib/components/TextArea.svelte";

	export let value = {}

	let inputName: string = "";
	let inputDescription: string = "";

	$: value = {
		name: inputName,
		description: inputDescription,
	}
</script>

<div class="flex flex-col">
	<h2>Certificate</h2>
	<InputText label="Name" bind:value={inputName}/>
	<TextArea label="Description" bind:value={inputDescription}/>
</div>
