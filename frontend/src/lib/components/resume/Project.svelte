<script>
	import InputDate from "./InputDate.svelte";
	import InputText from "./InputText.svelte";
</script>

<div class="flex flex-col">
	<InputText label="Title"></InputText>
	<InputText label="Subtitle"></InputText>
	<InputDate label="Start Date"></InputDate>
	<InputDate label="End Date"></InputDate>
	<InputText label="Description"></InputText>
</div>
