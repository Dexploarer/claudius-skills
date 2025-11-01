---
name: react-native-component-generator
description: Generates React Native components with platform-specific code, TypeScript support, and mobile-first patterns. Use when user asks to "create React Native component", "generate RN component", "scaffold mobile component", or "create cross-platform component".
allowed-tools: [Write, Read, Glob]
---

# React Native Component Generator

Generates React Native components with platform-specific optimizations, TypeScript support, and mobile best practices.

## When to Use

- "Create a React Native Button component"
- "Generate mobile component"
- "Scaffold cross-platform component"
- "Create RN component with platform code"
- "Generate native module wrapper"

## Instructions

### 1. Gather Requirements

Ask for:
- Component name (PascalCase)
- Platform support (iOS, Android, or both)
- Props and their types
- Native modules needed
- Styling approach (StyleSheet, styled-components, etc.)
- Animations needed

### 2. Generate Base Component

**Basic Functional Component:**
```typescript
// components/Button/Button.tsx
import React from 'react';
import {
  TouchableOpacity,
  Text,
  StyleSheet,
  TouchableOpacityProps,
  ViewStyle,
  TextStyle,
} from 'react-native';

interface ButtonProps extends TouchableOpacityProps {
  title: string;
  onPress: () => void;
  variant?: 'primary' | 'secondary' | 'outline';
  size?: 'small' | 'medium' | 'large';
}

export const Button: React.FC<ButtonProps> = ({
  title,
  onPress,
  variant = 'primary',
  size = 'medium',
  style,
  ...props
}) => {
  return (
    <TouchableOpacity
      style={[
        styles.button,
        styles[variant],
        styles[size],
        style,
      ]}
      onPress={onPress}
      activeOpacity={0.7}
      {...props}
    >
      <Text style={[styles.text, styles[`${variant}Text`]]}>
        {title}
      </Text>
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  button: {
    borderRadius: 8,
    justifyContent: 'center',
    alignItems: 'center',
  },
  primary: {
    backgroundColor: '#007AFF',
  },
  secondary: {
    backgroundColor: '#6c757d',
  },
  outline: {
    backgroundColor: 'transparent',
    borderWidth: 1,
    borderColor: '#007AFF',
  },
  small: {
    paddingVertical: 8,
    paddingHorizontal: 16,
  },
  medium: {
    paddingVertical: 12,
    paddingHorizontal: 24,
  },
  large: {
    paddingVertical: 16,
    paddingHorizontal: 32,
  },
  text: {
    fontSize: 16,
    fontWeight: '600',
  },
  primaryText: {
    color: '#ffffff',
  },
  secondaryText: {
    color: '#ffffff',
  },
  outlineText: {
    color: '#007AFF',
  },
});
```

**Component with State and Hooks:**
```typescript
// components/SearchInput/SearchInput.tsx
import React, { useState, useCallback, useEffect } from 'react';
import {
  TextInput,
  View,
  StyleSheet,
  TextInputProps,
  TouchableOpacity,
  ActivityIndicator,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';

interface SearchInputProps extends Omit<TextInputProps, 'onChangeText'> {
  onSearch: (query: string) => void;
  onClear?: () => void;
  debounceMs?: number;
  loading?: boolean;
}

export const SearchInput: React.FC<SearchInputProps> = ({
  onSearch,
  onClear,
  debounceMs = 300,
  loading = false,
  placeholder = 'Search...',
  ...props
}) => {
  const [query, setQuery] = useState('');

  useEffect(() => {
    const timer = setTimeout(() => {
      if (query) {
        onSearch(query);
      }
    }, debounceMs);

    return () => clearTimeout(timer);
  }, [query, debounceMs, onSearch]);

  const handleClear = useCallback(() => {
    setQuery('');
    onClear?.();
  }, [onClear]);

  return (
    <View style={styles.container}>
      <Ionicons name="search" size={20} color="#666" style={styles.icon} />
      <TextInput
        style={styles.input}
        value={query}
        onChangeText={setQuery}
        placeholder={placeholder}
        placeholderTextColor="#999"
        autoCapitalize="none"
        autoCorrect={false}
        {...props}
      />
      {loading && <ActivityIndicator size="small" color="#007AFF" />}
      {query.length > 0 && !loading && (
        <TouchableOpacity onPress={handleClear}>
          <Ionicons name="close-circle" size={20} color="#666" />
        </TouchableOpacity>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#f0f0f0',
    borderRadius: 10,
    paddingHorizontal: 12,
    height: 44,
  },
  icon: {
    marginRight: 8,
  },
  input: {
    flex: 1,
    fontSize: 16,
    color: '#000',
  },
});
```

### 3. Platform-Specific Code

**Using Platform Module:**
```typescript
// components/Header/Header.tsx
import React from 'react';
import { View, Text, StyleSheet, Platform, StatusBar } from 'react-native';

interface HeaderProps {
  title: string;
}

export const Header: React.FC<HeaderProps> = ({ title }) => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>{title}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    paddingTop: Platform.select({
      ios: 50,
      android: StatusBar.currentHeight || 0,
      default: 0,
    }),
    paddingBottom: 10,
    paddingHorizontal: 16,
    backgroundColor: '#007AFF',
    ...Platform.select({
      ios: {
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.1,
        shadowRadius: 4,
      },
      android: {
        elevation: 4,
      },
    }),
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#fff',
    ...Platform.select({
      ios: {
        fontFamily: 'System',
      },
      android: {
        fontFamily: 'Roboto',
      },
    }),
  },
});
```

**Using Platform-Specific Files:**
```typescript
// components/DatePicker/DatePicker.ios.tsx
import React from 'react';
import { DatePickerIOS } from '@react-native-community/datetimepicker';

interface DatePickerProps {
  date: Date;
  onDateChange: (date: Date) => void;
}

export const DatePicker: React.FC<DatePickerProps> = ({ date, onDateChange }) => {
  return <DatePickerIOS date={date} onDateChange={onDateChange} mode="date" />;
};
```

```typescript
// components/DatePicker/DatePicker.android.tsx
import React, { useState } from 'react';
import { TouchableOpacity, Text, StyleSheet } from 'react-native';
import DateTimePicker from '@react-native-community/datetimepicker';

interface DatePickerProps {
  date: Date;
  onDateChange: (date: Date) => void;
}

export const DatePicker: React.FC<DatePickerProps> = ({ date, onDateChange }) => {
  const [show, setShow] = useState(false);

  const onChange = (_event: any, selectedDate?: Date) => {
    setShow(false);
    if (selectedDate) {
      onDateChange(selectedDate);
    }
  };

  return (
    <>
      <TouchableOpacity onPress={() => setShow(true)} style={styles.button}>
        <Text>{date.toLocaleDateString()}</Text>
      </TouchableOpacity>
      {show && (
        <DateTimePicker value={date} mode="date" display="default" onChange={onChange} />
      )}
    </>
  );
};

const styles = StyleSheet.create({
  button: {
    padding: 12,
    backgroundColor: '#f0f0f0',
    borderRadius: 8,
  },
});
```

```typescript
// components/DatePicker/index.ts
export { DatePicker } from './DatePicker';
```

### 4. Animated Components

**Basic Animation:**
```typescript
// components/FadeIn/FadeIn.tsx
import React, { useEffect, useRef } from 'react';
import { Animated, ViewProps } from 'react-native';

interface FadeInProps extends ViewProps {
  duration?: number;
  delay?: number;
}

export const FadeIn: React.FC<FadeInProps> = ({
  children,
  duration = 300,
  delay = 0,
  style,
  ...props
}) => {
  const fadeAnim = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    Animated.timing(fadeAnim, {
      toValue: 1,
      duration,
      delay,
      useNativeDriver: true,
    }).start();
  }, [fadeAnim, duration, delay]);

  return (
    <Animated.View style={[style, { opacity: fadeAnim }]} {...props}>
      {children}
    </Animated.View>
  );
};
```

**Complex Animation:**
```typescript
// components/SlideUp/SlideUp.tsx
import React, { useEffect, useRef } from 'react';
import { Animated, Dimensions } from 'react-native';

const { height } = Dimensions.get('window');

interface SlideUpProps {
  visible: boolean;
  onClose: () => void;
  children: React.ReactNode;
}

export const SlideUp: React.FC<SlideUpProps> = ({ visible, onClose, children }) => {
  const slideAnim = useRef(new Animated.Value(height)).current;

  useEffect(() => {
    if (visible) {
      Animated.spring(slideAnim, {
        toValue: 0,
        useNativeDriver: true,
        tension: 65,
        friction: 11,
      }).start();
    } else {
      Animated.timing(slideAnim, {
        toValue: height,
        duration: 250,
        useNativeDriver: true,
      }).start();
    }
  }, [visible, slideAnim]);

  if (!visible) return null;

  return (
    <Animated.View
      style={{
        position: 'absolute',
        bottom: 0,
        left: 0,
        right: 0,
        backgroundColor: '#fff',
        borderTopLeftRadius: 20,
        borderTopRightRadius: 20,
        padding: 20,
        transform: [{ translateY: slideAnim }],
      }}
    >
      {children}
    </Animated.View>
  );
};
```

### 5. List Components

**Optimized FlatList:**
```typescript
// components/UserList/UserList.tsx
import React, { useCallback } from 'react';
import {
  FlatList,
  View,
  Text,
  StyleSheet,
  ActivityIndicator,
  RefreshControl,
} from 'react-native';

interface User {
  id: string;
  name: string;
  email: string;
}

interface UserListProps {
  users: User[];
  loading?: boolean;
  onRefresh?: () => void;
  onEndReached?: () => void;
  refreshing?: boolean;
}

export const UserList: React.FC<UserListProps> = ({
  users,
  loading,
  onRefresh,
  onEndReached,
  refreshing = false,
}) => {
  const renderItem = useCallback(({ item }: { item: User }) => (
    <View style={styles.item}>
      <Text style={styles.name}>{item.name}</Text>
      <Text style={styles.email}>{item.email}</Text>
    </View>
  ), []);

  const keyExtractor = useCallback((item: User) => item.id, []);

  const renderFooter = useCallback(() => {
    if (!loading) return null;
    return (
      <View style={styles.footer}>
        <ActivityIndicator size="small" color="#007AFF" />
      </View>
    );
  }, [loading]);

  const renderEmpty = useCallback(() => (
    <View style={styles.empty}>
      <Text style={styles.emptyText}>No users found</Text>
    </View>
  ), []);

  return (
    <FlatList
      data={users}
      renderItem={renderItem}
      keyExtractor={keyExtractor}
      ListFooterComponent={renderFooter}
      ListEmptyComponent={renderEmpty}
      onEndReached={onEndReached}
      onEndReachedThreshold={0.5}
      refreshControl={
        onRefresh ? (
          <RefreshControl refreshing={refreshing} onRefresh={onRefresh} />
        ) : undefined
      }
      removeClippedSubviews={true}
      maxToRenderPerBatch={10}
      updateCellsBatchingPeriod={50}
      initialNumToRender={10}
      windowSize={5}
    />
  );
};

const styles = StyleSheet.create({
  item: {
    padding: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#e0e0e0',
  },
  name: {
    fontSize: 16,
    fontWeight: '600',
    marginBottom: 4,
  },
  email: {
    fontSize: 14,
    color: '#666',
  },
  footer: {
    paddingVertical: 20,
    alignItems: 'center',
  },
  empty: {
    padding: 40,
    alignItems: 'center',
  },
  emptyText: {
    fontSize: 16,
    color: '#999',
  },
});
```

### 6. Form Components

**Input with Validation:**
```typescript
// components/TextInputField/TextInputField.tsx
import React, { useState } from 'react';
import { View, TextInput, Text, StyleSheet, TextInputProps } from 'react-native';

interface TextInputFieldProps extends TextInputProps {
  label: string;
  error?: string;
  required?: boolean;
  validate?: (value: string) => string | undefined;
}

export const TextInputField: React.FC<TextInputFieldProps> = ({
  label,
  error,
  required,
  validate,
  onBlur,
  onChangeText,
  ...props
}) => {
  const [localError, setLocalError] = useState<string>();

  const handleBlur = (e: any) => {
    if (validate && props.value) {
      setLocalError(validate(props.value));
    }
    onBlur?.(e);
  };

  const handleChange = (text: string) => {
    setLocalError(undefined);
    onChangeText?.(text);
  };

  const displayError = error || localError;

  return (
    <View style={styles.container}>
      <Text style={styles.label}>
        {label}
        {required && <Text style={styles.required}> *</Text>}
      </Text>
      <TextInput
        style={[styles.input, displayError && styles.inputError]}
        onBlur={handleBlur}
        onChangeText={handleChange}
        {...props}
      />
      {displayError && <Text style={styles.errorText}>{displayError}</Text>}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    marginBottom: 16,
  },
  label: {
    fontSize: 14,
    fontWeight: '600',
    marginBottom: 8,
    color: '#333',
  },
  required: {
    color: '#ff0000',
  },
  input: {
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 8,
    padding: 12,
    fontSize: 16,
    backgroundColor: '#fff',
  },
  inputError: {
    borderColor: '#ff0000',
  },
  errorText: {
    color: '#ff0000',
    fontSize: 12,
    marginTop: 4,
  },
});
```

### 7. Native Module Integration

**Using Native Modules:**
```typescript
// components/BiometricAuth/BiometricAuth.tsx
import React from 'react';
import { Alert, Platform } from 'react-native';
import TouchID from 'react-native-touch-id';
import ReactNativeBiometrics from 'react-native-biometrics';

interface BiometricAuthProps {
  onSuccess: () => void;
  onError: (error: string) => void;
}

export const useBiometricAuth = ({ onSuccess, onError }: BiometricAuthProps) => {
  const authenticate = async () => {
    try {
      if (Platform.OS === 'ios') {
        const isSupported = await TouchID.isSupported();
        if (!isSupported) {
          onError('Biometric authentication not supported');
          return;
        }

        await TouchID.authenticate('Authenticate to continue', {
          fallbackLabel: 'Use Passcode',
        });
        onSuccess();
      } else {
        const rnBiometrics = new ReactNativeBiometrics();
        const { available } = await rnBiometrics.isSensorAvailable();

        if (!available) {
          onError('Biometric authentication not available');
          return;
        }

        const { success } = await rnBiometrics.simplePrompt({
          promptMessage: 'Authenticate to continue',
        });

        if (success) {
          onSuccess();
        } else {
          onError('Authentication failed');
        }
      }
    } catch (error: any) {
      onError(error.message);
    }
  };

  return { authenticate };
};
```

### 8. Responsive Components

**Using Dimensions:**
```typescript
// components/ResponsiveCard/ResponsiveCard.tsx
import React from 'react';
import { View, Text, StyleSheet, Dimensions, ScaledSize } from 'react-native';
import { useDeviceOrientation } from '@react-native-community/hooks';

const getStyles = (window: ScaledSize) => {
  const { width } = window;
  const isTablet = width >= 768;

  return StyleSheet.create({
    card: {
      padding: isTablet ? 24 : 16,
      margin: isTablet ? 16 : 8,
      backgroundColor: '#fff',
      borderRadius: isTablet ? 12 : 8,
      shadowColor: '#000',
      shadowOffset: { width: 0, height: 2 },
      shadowOpacity: 0.1,
      shadowRadius: 4,
      elevation: 3,
    },
    title: {
      fontSize: isTablet ? 24 : 18,
      fontWeight: 'bold',
      marginBottom: isTablet ? 12 : 8,
    },
  });
};

export const ResponsiveCard: React.FC<{ title: string; children: React.ReactNode }> = ({
  title,
  children,
}) => {
  const window = Dimensions.get('window');
  const styles = getStyles(window);

  return (
    <View style={styles.card}>
      <Text style={styles.title}>{title}</Text>
      {children}
    </View>
  );
};
```

### 9. Index File

Create barrel export:

```typescript
// components/index.ts
export { Button } from './Button/Button';
export { SearchInput } from './SearchInput/SearchInput';
export { Header } from './Header/Header';
export { DatePicker } from './DatePicker';
export { FadeIn } from './FadeIn/FadeIn';
export { SlideUp } from './SlideUp/SlideUp';
export { UserList } from './UserList/UserList';
export { TextInputField } from './TextInputField/TextInputField';
export { ResponsiveCard } from './ResponsiveCard/ResponsiveCard';
```

### 10. Tests

**Component Test:**
```typescript
// components/Button/__tests__/Button.test.tsx
import React from 'react';
import { render, fireEvent } from '@testing-library/react-native';
import { Button } from '../Button';

describe('Button', () => {
  it('renders correctly', () => {
    const { getByText } = render(<Button title="Click me" onPress={() => {}} />);
    expect(getByText('Click me')).toBeTruthy();
  });

  it('calls onPress when pressed', () => {
    const onPress = jest.fn();
    const { getByText } = render(<Button title="Click me" onPress={onPress} />);

    fireEvent.press(getByText('Click me'));
    expect(onPress).toHaveBeenCalledTimes(1);
  });

  it('applies correct variant styles', () => {
    const { getByText, rerender } = render(
      <Button title="Primary" onPress={() => {}} variant="primary" />
    );

    let button = getByText('Primary').parent;
    expect(button?.props.style).toContainEqual(
      expect.objectContaining({ backgroundColor: '#007AFF' })
    );

    rerender(<Button title="Outline" onPress={() => {}} variant="outline" />);

    button = getByText('Outline').parent;
    expect(button?.props.style).toContainEqual(
      expect.objectContaining({ backgroundColor: 'transparent' })
    );
  });
});
```

### Best Practices

**DO:**
- Use TypeScript for type safety
- Optimize FlatList performance
- Use Platform-specific code when needed
- Implement proper keyboard handling
- Use useCallback for list renders
- Test on both platforms
- Follow platform design guidelines

**DON'T:**
- Use inline styles in render
- Forget to use useNativeDriver for animations
- Ignore safe area insets
- Over-render components
- Use ScrollView for long lists
- Hardcode dimensions
- Ignore accessibility

## Checklist

- [ ] Component created with TypeScript
- [ ] Props interface defined
- [ ] Platform-specific code handled
- [ ] Styles optimized with StyleSheet
- [ ] Accessibility props added
- [ ] Tests written
- [ ] Index file updated
- [ ] Performance optimized
- [ ] Documentation added
