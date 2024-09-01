<script>
    import { onMount } from "svelte";
	import TextArea from "./TextArea.svelte";
	import InputText from "./InputText.svelte";
	import InputDate from "./InputDate.svelte";
    
    onMount(async () => {
      
    });
  </script>

<div class="professional-exp">
    <h2>Professional Experience</h2>
    <form>
        <label for="job-title">Job Title</label>
        <InputText />
        <label for="employer">Employer</label>
        <InputText />
        <label for="city">City</label>
        <InputText/>
        <label for="country">Country</label>
        <InputText/>
        <label for="start_date">Start Date</label>
        <InputDate />
        <label for="end_date">End Date</label>
        <InputDate />
        <label for="description">Description</label>
        <TextArea />
    </form>
</div>