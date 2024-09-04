<script lang="ts">
	import InputText from "$lib/components/InputText.svelte";
	import type Link from "$lib/interfaces/resume/Link";

	export let value: Link | null = null;

	let title: string = "";
	let url: string = "";

	$: value = {
		title,
		url
	};
</script>

<div class="flex flex-col">
	<h2>Link</h2>
	<InputText label="Title" bind:value={title} />
	<InputText label="URL" bind:value={url} />
</div>
