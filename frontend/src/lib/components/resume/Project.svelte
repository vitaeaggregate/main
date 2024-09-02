<script>
	import InputText from "$lib/components/InputText.svelte";
	import InputDate from "$lib/components/InputDate.svelte";
</script>

<div class="flex flex-col">
	<InputText label="Title"></InputText>
	<InputText label="Subtitle"></InputText>
	<InputDate label="Start Date"></InputDate>
	<InputDate label="End Date"></InputDate>
	<InputText label="Description"></InputText>
</div>
