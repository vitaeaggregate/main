<script>
    // import {onMount} from "svelte"
    import InputText from "./resume/InputText.svelte";
    import TextArea from "./resume/TextArea.svelte";
    // import PersonalInfo from "$lib/interfaces/personal_info";
    // import Skill from "$lib/interfaces/skill"
    // onMount(async () => {
    //     const data = await fetch();
    // })
</script>

<div class="flex flex-col">
    <h2>Skills</h2>
    <InputText label="Name"/>
    <TextArea label="Description"/>
    <InputText label="Skill Level"/>
</div>