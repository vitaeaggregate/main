<script lang='ts'>
	import { createEventDispatcher } from "svelte";
	import InputText from "./InputText.svelte";

	let resumeID: number = 0;
	let inputName: string = '';
	let inputJobTitle: string = '';
	let inputOrganization: string = '';
	let inputEmail: string = '';
	let inputPhone: string = '';

	$: reference = {
		resume: resumeID,
		name: inputName,
		job_title: inputJobTitle,
		organization: inputOrganization,
		email: inputEmail,
		phone: inputPhone,
	}

	$: console.log(reference)

	const dispatch = createEventDispatcher();
	$: {
		dispatch("update", reference);
	}

</script>

<div class="flex flex-col">
	<h2>Reference</h2>
	<InputText label="Name" bind:value={inputName}/>
	<InputText label="Job Title" bind:value={inputJobTitle}/>
	<InputText label="Organization" bind:value={inputOrganization}/>
	<InputText label="Email" bind:value={inputEmail}/>
	<InputText label="Phone" bind:value={inputPhone}/>
</div>