<script lang='ts'>
	import { createEventDispatcher } from "svelte";
    import InputText from "./resume/InputText.svelte";
    import TextArea from "./resume/TextArea.svelte";

    let resumeID: number = 0;
    let inputName: string = '';
    let inputDescription: string = '';

    $: interest = {
        resume: resumeID,
        name: inputName,
        description: inputDescription,
    }

    const dispatch = createEventDispatcher();
    $: {
        dispatch("update", interest);
    }

</script>

<div class="flex flex-col">
    <h2>Interest</h2>
    <InputText label="Name" bind:value={inputName}/>
    <TextArea label="Description" bind:value={inputDescription}/>
</div>