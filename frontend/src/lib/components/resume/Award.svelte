<script lang="ts">
	import InputText from "$lib/components/InputText.svelte";
	import InputDate from "$lib/components/InputDate.svelte";
	import TextArea from "$lib/components/TextArea.svelte";
	import type Award from "$lib/interfaces/resume/Award";
	import { getRandomId } from "$lib/utils";
	import { onMount } from "svelte";

	export let value: Award = {
		title: "",
		issuer: "",
		description: "",
		date: ""
	};
	export let readOnly: boolean = false;

	onMount(() => {
		if (value.id) return;
		value.id = getRandomId();
	});
</script>

{#if readOnly}
	<div>
		<p><strong>Title:</strong> {value.title ? value.title : ""}</p>
		<p><strong>Issuer:</strong> {value.issuer ? value.issuer : ""}</p>
		<p><strong>Date:</strong> {value.date ? value.date : ""}</p>
		<p><strong>Description:</strong> {value.description ? value.description : ""}</p>
	</div>
{:else}
	<div>
		<InputText label="Title" bind:value={value.title} />
		<InputText label="Issuer" bind:value={value.issuer} />
		<InputDate label="Date" bind:value={value.date} />
		<TextArea label="Description" bind:value={value.description} />
	</div>
{/if}
