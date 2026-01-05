from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, mean_squared_error, accuracy_score

wineData = load_wine()
X = wineData.data
y = wineData.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)

y_prediction = dt.predict(X_test)

conf_matrix = confusion_matrix(y_test, y_prediction)
mse = mean_squared_error(y_test, y_prediction)
accuracy = accuracy_score(y_test, y_prediction)

print("Confusion Matrix:")
print(conf_matrix)
print(f"Mean Squared Error: {mse:.4f}")
print(f"Accuracy: {accuracy:.4f}")