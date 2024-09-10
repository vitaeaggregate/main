<script lang="ts">
	import { createEventDispatcher } from "svelte";
	import InputText from "$lib/components/InputText.svelte";
	import type Reference from "$lib/interfaces/resume/Reference";
	import { getRandomId } from "$lib/utils";
	import { onMount } from "svelte";

	export let value: Reference = {
		name: "",
		job_title: "",
		organization: "",
		email: "",
		phone: ""
	};
	export let readOnly: boolean = false;

	onMount(() => {
		if (value.id) return;
		value.id = getRandomId();
	});
</script>

{#if readOnly}
	<div>
		<p><strong>Name:</strong> {value.name ? value.name : ""}</p>
		<p><strong>Job Title:</strong> {value.job_title ? value.job_title : ""}</p>
		<p><strong>Organization:</strong> {value.organization ? value.organization : ""}</p>
		<p><strong>Email:</strong> {value.email ? value.email : ""}</p>
		<p><strong>Phone:</strong> {value.phone ? value.phone : ""}</p>
	</div>
{:else}
	<div>
		<p class='req'>*</p>
		<InputText label="Name" bind:value={value.name} />
		<InputText label="Job Title" bind:value={value.job_title} />
		<InputText label="Organization" bind:value={value.organization} />
		<InputText label="Email" bind:value={value.email} />
		<InputText label="Phone" bind:value={value.phone} />
	</div>
{/if}
