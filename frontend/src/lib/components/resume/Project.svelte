<script lang="ts">
	import InputText from "$lib/components/InputText.svelte";
	import InputDate from "$lib/components/InputDate.svelte";
	import type Project from "$lib/interfaces/resume/Project";
	import { getRandomId } from "$lib/utils";
	import { onMount } from "svelte";
	import TextArea from "$lib/components/TextArea.svelte";

	export let value: Project = {
		title: "",
		sub_title: "",
		start_date: undefined,
		end_date: undefined,
		description: ""
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
		<p><strong>Subtitle:</strong> {value.sub_title ? value.sub_title : ""}</p>
		<p><strong>Start Date:</strong> {value.start_date ? value.start_date : ""}</p>
		<p><strong>End Date:</strong> {value.end_date ? value.end_date : ""}</p>
		<p><strong>Description:</strong> {value.description ? value.description : ""}</p>
	</div>
{:else}
	<div>
		<p class='req'>*</p>
		<InputText label="Title" bind:value={value.title} />
		<InputText label="Subtitle" bind:value={value.sub_title} />
		<InputDate label="Start Date" bind:value={value.start_date} />
		<InputDate label="End Date" bind:value={value.end_date} />
		<p class='req'>*</p>
		<TextArea label="Description" bind:value={value.description} />
	</div>
{/if}
