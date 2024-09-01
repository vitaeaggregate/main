<script>
    import InputText from "./resume/InputText.svelte";
    import TextArea from "./resume/TextArea.svelte";
    // import {onMount} from "svelte"
    // import Interest from "$lib/interfaces/interest"
    // onMount(async () => {
    //     const data = await fetch();
    // })
</script>

<div class="flex flex-col">
    <h2>Interest</h2>
    <InputText label="Name"/>
    <TextArea label="Description"/>
</div>