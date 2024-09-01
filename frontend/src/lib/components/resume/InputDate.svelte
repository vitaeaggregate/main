<script lang="ts">
	export let label: string = "Input Date";
	export let placeholder: string = label;
</script>

<label class="flex flex-col">
	{label}:
	<input type="date" {placeholder} class="border-2" />
</label>
