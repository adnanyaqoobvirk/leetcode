with CustomerContacts AS (
    SELECT
        customer_id,
        COUNT(user_id) AS contacts_cnt
    FROM
        Customers
        LEFT JOIN
        Contacts
        ON
            customer_id = user_id
    GROUP BY
        customer_id
), CustomerTrustedContacts AS (
    SELECT
        customer_id,
        COUNT(user_id) AS trusted_contacts_cnt
    FROM
        Customers
        LEFT JOIN
        Contacts
        ON
            customer_id = user_id
            AND
            contact_email IN (SELECT email FROM Customers)
    GROUP BY
        customer_id
)

SELECT
    I.invoice_id,
    C.customer_name,
    I.price,
    CC.contacts_cnt,
    CT.trusted_contacts_cnt
FROM
    Invoices AS I
    INNER JOIN
    Customers AS C
    ON
        I.user_id = C.customer_id
    INNER JOIN
    CustomerContacts AS CC
    ON
        CC.customer_id = C.customer_id
    INNER JOIN
    CustomerTrustedContacts AS CT
    ON
        CT.customer_id = C.customer_id
ORDER BY
    invoice_id ASC
    
