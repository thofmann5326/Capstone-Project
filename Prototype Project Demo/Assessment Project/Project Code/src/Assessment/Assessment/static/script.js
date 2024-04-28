function handleCustomerChange(select) {
    const selectedCustomerId = select.value;
    window.location.href = `/technology-inventory/?customer=${selectedCustomerId}`;
}
