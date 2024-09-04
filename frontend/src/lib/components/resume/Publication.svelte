<script lang='ts'>
    import TextArea from "$lib/components/TextArea.svelte";
    import InputText from "$lib/components/InputText.svelte";
    import InputDate from "$lib/components/InputDate.svelte";

    export let value = {};

	let inputTitle: string = "";
	let inputPublisher: string = "";
	let inputDate: Date;
	let inputDescription: string = "";

    $: value = {
        title: inputTitle,
        publisher: inputPublisher,
        date: inputDate,
        description: inputDescription,
    }
</script>

<div class="flex flex-col">
    <h2>Publications</h2>
    <InputText label="Title" bind:value={inputTitle}/>
    <InputText label="Publisher" bind:value={inputPublisher}/>
    <InputDate label="Date" bind:value={inputDate}/>
    <TextArea label="Description" bind:value={inputDescription}/>
</div>