<script lang="ts">
	import InputText from "$lib/components/InputText.svelte";
	import type Link from "$lib/interfaces/resume/Link";
	import { getRandomId } from "$lib/utils";
	import { onMount } from "svelte";

	export let value: Link = {
		title: "",
		url: ""
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
		<p><strong>URL:</strong> {value.url ? value.url : ""}</p>
	</div>
{:else}
	<div>
		<p class='req'>*</p>
		<InputText label="Title" bind:value={value.title} />
		<p class='req'>*</p>
		<InputText label="URL" bind:value={value.url} />
	</div>
{/if}
