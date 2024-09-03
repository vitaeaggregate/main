<script lang='ts'>
    import InputText from "$lib/components/InputText.svelte";
	import { createEventDispatcher } from "svelte";
    
    let resumeID: number = 0;
    let inputTitle: string = '';
    let inputURL: string = '';

    $: linksObject = {
        resume: resumeID,
        title: inputTitle,
        url: inputURL,
    }

    // $: console.log(linksObject);

    const dispatch = createEventDispatcher();
    $: {
        dispatch("update", linksObject)
    }
</script>

<div class="flex flex-col">
    <h2>Links</h2>
    <InputText label="Title" bind:value={inputTitle}/>
    <InputText label="URL" bind:value={inputURL}/>
</div>