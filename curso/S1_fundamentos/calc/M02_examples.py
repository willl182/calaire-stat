"""Reproducible numerical examples for M02; all inputs are simulated."""

import numpy as np


def describe(values):
    values = np.asarray(values, dtype=float)
    return {
        "n": values.size,
        "mean": float(np.mean(values)),
        "median": float(np.median(values)),
        "variance_sample": float(np.var(values, ddof=1)),
        "sd_sample": float(np.std(values, ddof=1)),
        "range": float(np.ptp(values)),
        "q1_linear": float(np.quantile(values, 0.25, method="linear")),
        "q3_linear": float(np.quantile(values, 0.75, method="linear")),
        "se_mean": float(np.std(values, ddof=1) / np.sqrt(values.size)),
    }


# Simulated eight readings in one level and one day (nmol/mol).
readings = np.array([100.1, 100.4, 99.9, 100.2, 100.5, 100.0, 100.3, 99.8])
print("B one-day readings (nmol/mol)", describe(readings))
histogram_counts = np.histogram(readings, bins=[99.7, 100.0, 100.3, 100.6])[0]
print("B histogram bins [99.7, 100.0, 100.3, 100.6] counts",
      histogram_counts.tolist())
print("B histogram relative frequencies", (histogram_counts / readings.size).tolist())
print("B CV percent", 100 * np.std(readings, ddof=1) / np.mean(readings))

# Simulated paired reference and indication values over three days.
reference = np.array([80.0, 80.0, 200.0, 200.0, 420.0, 420.0])
indication = np.array([80.2, 80.1, 199.9, 200.1, 420.3, 420.1])
error = indication - reference
print("B multi-day reference", describe(reference))
print("B multi-day indication", describe(indication))
print("B multi-day errors", error.tolist(), describe(error))
for day, values in enumerate(error.reshape(3, 2), start=1):
    print(f"B day {day} error mean and sample SD", float(np.mean(values)),
          float(np.std(values, ddof=1)))
print("B zero reading (simulated, nmol/mol)", -0.2)
zero_values = np.array([-0.2, -0.1, 0.0, 0.1, 0.2])
zero_truncated = zero_values.copy()
zero_truncated[zero_truncated < 0] = 0.0
print("B zero values signed and after truncation", zero_values.tolist(),
      zero_truncated.tolist())
print("B zero means signed and after truncation", float(np.mean(zero_values)),
      float(np.mean(zero_truncated)))

# Effect of rounding the six simulated errors before calculating their mean.
rounded_errors = np.rint(error)
print("B six-error mean without intermediate rounding", float(np.mean(error)))
print("B six-error mean after rounding each error to integer",
      float(np.mean(rounded_errors)))

# Simulated within-day values for a median absolute deviation example.
mad_values = np.array([0.1, 0.2, 0.2, 0.3, 0.9])
mad_center = float(np.median(mad_values))
absolute_deviations = np.abs(mad_values - mad_center)
print("I MAD example values", mad_values.tolist())
print("I MAD example median and absolute deviations", mad_center,
      absolute_deviations.tolist())
print("I MAD example", float(np.median(absolute_deviations)))

# Simulated errors across reference values for the descriptive linear-error model.
x = np.array([80.0, 160.0, 240.0, 320.0, 400.0])
e = np.array([0.23, 0.42, 0.58, 0.78, 0.88])
slope, intercept = np.polyfit(x, e, 1)
predicted = intercept + slope * x
print("I x (nmol/mol)", x.tolist())
print("I errors (nmol/mol)", e.tolist())
print("I fitted intercept and error slope", float(intercept), float(slope))
print("I fitted predicted errors", predicted.tolist())
print("I fitted absolute indication slope (1 + error slope)", float(1 + slope))

# Simulated signed errors: two groups with opposite biases and one influential value.
group_1 = np.array([0.4, 0.5, 0.3, 0.4])
group_2 = np.array([-0.4, -0.5, -0.3, -0.4])
combined = np.concatenate([group_1, group_2])
with_influential = np.append(combined, 1.8)
for label, values in (("A group 1", group_1), ("A group 2", group_2),
                      ("A combined", combined), ("A combined plus influential", with_influential)):
    median = float(np.median(values))
    mad = float(np.median(np.abs(values - median)))
    print(label, "n", values.size, "mean signed", float(np.mean(values)),
          "mean absolute", float(np.mean(np.abs(values))),
          "absolute signed mean", float(abs(np.mean(values))),
          "median", median, "MAD", mad, "sample SD", float(np.std(values, ddof=1)))
