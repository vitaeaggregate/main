<script lang="ts">
	import InputText from "$lib/components/InputText.svelte";
	import InputDate from "$lib/components/InputDate.svelte";
	import TextArea from "$lib/components/TextArea.svelte";

	export let value = {};

	let inputTitle: string = "";
	let inputIssuer: string = "";
	let inputDate: Date;
	let inputDescription: string = "";

	$: value = {
		title: inputTitle,
		issuer: inputIssuer,
		date: inputDate,
		description: inputDescription
	};
</script>

<div class="flex flex-col">
	<h2>Award</h2>
	<InputText label="Title" bind:value={inputTitle} />
	<InputText label="Issuer" bind:value={inputIssuer} />
	<InputDate label="Date" bind:value={inputDate} />
	<TextArea label="Description" bind:value={inputDescription} />
</div>
