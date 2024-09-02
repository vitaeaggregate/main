<script lang="ts">
	export let label: string = "Input Text";
	export let placeholder: string = label;

	export let value: string;

</script>

<label class="flex flex-col">
	{label}:
	<input type="text" bind:value={value} {placeholder} class="border-2"/>
</label>
