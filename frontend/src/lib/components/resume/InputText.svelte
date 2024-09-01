<script lang="ts">
	export let label: string = "Input Text";
	export let placeholder: string = label;
</script>

<label class="flex flex-col">
	{label}:
	<input type="text" {placeholder} class="border-2" />
</label>
