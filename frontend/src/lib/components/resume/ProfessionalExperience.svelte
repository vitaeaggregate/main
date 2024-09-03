<script lang='ts'>
	import TextArea from "$lib/components/TextArea.svelte";
	import InputText from "$lib/components/InputText.svelte";
	import InputDate from "$lib/components/InputDate.svelte";
	import { createEventDispatcher } from "svelte";

    let resumeID: number = 0;
    let inputJobTitle: string = '';
    let inputEmployer: string = '';
    let inputCity: string = '';
    let inputCountry: string = '';
    let inputStartDate: Date = new Date;
    let inputEndDate: Date = new Date;
    let inputDescription: string = '';

    $: professionalExperience = {
        resume: resumeID,
        job_title: inputJobTitle,
        employer: inputEmployer,
        city: inputCity,
        country: inputCountry,
        start_date: inputStartDate,
        end_date: inputEndDate,
        description: inputDescription,
    }

    const dispatch = createEventDispatcher();
    $: {
        dispatch("update", professionalExperience);
    }
</script>

<div class="flex flex-col">
    <h2>Professional Experience</h2>
    <InputText label="Job Title" bind:value={inputJobTitle}/>
    <InputText label="Employer" bind:value={inputEmployer}/>
    <InputText label="City" bind:value={inputCity}/>
    <InputText label="Country" bind:value={inputCountry}/>
    <InputDate label="Start Date" bind:value={inputStartDate}/>
    <InputDate label="End Date" bind:value={inputEndDate}/>
    <TextArea label="Description" bind:value={inputDescription}/>
</div>
