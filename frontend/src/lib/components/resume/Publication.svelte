<script lang='ts'>
    import TextArea from "$lib/components/TextArea.svelte";
    import InputText from "$lib/components/InputText.svelte";
    import InputDate from "$lib/components/InputDate.svelte";
	import { createEventDispatcher } from "svelte";

    let resumeID: number = 0;
	let inputTitle: string = '';
	let inputPublisher: string = '';
	let inputDate: Date = new Date;
	let inputDescription: string = '';

    $: publication = {
        resume: resumeID,
        title: inputTitle,
        publisher: inputPublisher,
        date: inputDate,
        description: inputDescription,
    }
 
    const dispatch = createEventDispatcher();
    $: {
        dispatch("update", publication);
    }
</script>

<div class="flex flex-col">
    <h2>Publications</h2>
    <InputText label="Title" bind:value={inputTitle}/>
    <InputText label="Publisher" bind:value={inputPublisher}/>
    <InputDate label="Date" bind:value={inputDate}/>
    <TextArea label="Description" bind:value={inputDescription}/>
</div>